class singleton(object):

    def __new__(cls, *args, **kawrgs):
        if '_inst' not in vars(cls):
            cls._inst = object.__new__(cls)
        return cls._inst


# 싱글톤 객체 생성.

class BaseFramer(object):

    def checkFrame(self):
        pass
    """
    올바른 Frame대로 왔는지 체크
    """

    