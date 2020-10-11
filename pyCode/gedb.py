import sys
sys.path.insert(0, '/opt/tiger/toutiao/webarch_lib')

from MySQLdb.infsec.sdk4dps import dps_token
from MySQLdb.auth import get_service_ip, get_user_pwd_dbname

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'usage:'
        print '      python2 gedb.py db_name'
        print 'db_name: 数据库名称'
        exit(-1)

    consul_name = 'toutiao.mysql.' + sys.argv[1] + '_read'
    hosts, ports = get_service_ip(consul_name)
    if not hosts or not ports:
        print '没有找到数据库的信息'
        exit(-1)

    p_psm = 'toutiao.unknown.unknown'
    token = dps_token.DpsToken().get_token()
    user, passwd, db = get_user_pwd_dbname(consul_name=consul_name, auth_key='', p_psm=p_psm, token=token)

    print 'host: %s' % hosts[0]
    print 'port: %s' % ports[0]
    print 'user: %s' % user
    print 'passwd: %s' % passwd
    print 'db: %s' % db
