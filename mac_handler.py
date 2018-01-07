import subprocess


class MacHandler(object):

    @staticmethod
    def register_hot_key():
        print 'not supported yet'

    @staticmethod
    def go_to(target):
        subprocess.call(["open", target])
