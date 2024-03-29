import requests
class Rest_Client:
    def __init__(self) -> None:
        self.base_url=base_url
        self.s=requests.session()
        pass
    '''
    这个类中重写了http的方法

    get
    process
    ……

    '''