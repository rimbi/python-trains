
class Setup(object):
    def __init__(self, config):
        self.config = config
    
    def get_distance(self, route):
        return int(self.config[2:])

if __name__ == '__main__':
    print 'Hello, world!'
