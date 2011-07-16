import sys
import yaml

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

from hamper import commands
from hamper.commander import CommanderFactory


if __name__ == '__main__':

    config = yaml.load(open('hamper.conf'))

    for key in ['server', 'port', 'nickname', 'channel']:
        if (key not in config) or (not config[key]):
            print('You need to define {0} in the config file.'.format(key))
            sys.exit();

    reactor.connectTCP(config['server'], config['port'],
            CommanderFactory(config['channel'], config['nickname']))
    reactor.run()
