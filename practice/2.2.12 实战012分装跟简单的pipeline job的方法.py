import requests


# 3 存储HTTP方法返回的响应
# Response 方法用来存放HTTP的响应(是个存储响应的容器)：
class Response:
    def __int__(self, code, body, raw_rasponse):
        self.code = code
        self.body = body
        self.raw_response = raw_rasponse

    def __repr__(self):
        return f"response code={self}\nresponse body={self.body}"


# 1
class Jenkins:
    def __int__(self, base_url, usename: None, password=None):
        self.base_url = base_url
        # 用rest client代替requests的session
        self.rest_client = RestClient(base_url)
        # 把self作为参数传给JenkinsOpertion
        self.use_jenkins = JenkinsOpertion(self)
        # crumb_field_name crumb_file_value作用是存储CSRF token的两个组成成分，CSRF token是由crumb_field_name 和crumber_filed_value
        self.crumb_field_name = None
        self.crumb_field_value = None
        if usename and password:
            self.login(usename, password)

    def login(self, username, password):
        self.rest_client.s.auth = username, password
        r = self.get_crumber_issuer()
        self.crumb_field_value = r.body['crumberRequesField']
        self.crumb_field_name = r.body['crumb']
        self.rest_client.s.headers[self.crumb_field_name] = self.crumb_field_name
        return self

    # get_crumber_issuer方法用来获取CSRF token
    def get_crumber_issuer(self):
        return self.rest_client.get("/crumberIssuer/api/json")

    def run_groovy(self, scrip):
        payload = {'scrop': scrip}
        return self.rest_client.post(f"/scriptText", data=payload)

    # 增加一个方法，用来检查目标job是否建立成功
    def get_job(self, job):
        return self.rest_client.get(f"/job/{job}/api/json")

    def list_jobs(self, attribute_to_show="name"):
        return self.s.get(f"/api/json?tree=jobs[{attribute_to_show}]")

    def get_user(self, username):
        return self.s.get(f"/user/{username}/api/json")


# 4 封装业务
class JenkinsOpertion:
    def __int__(self):
        self.jenkins = Jenkins

    def get_all_job_names(self):
        r = self.jenkins.list_jobs()
        jobs = [_['name'] for _ in r.body['jobs']]
        return jobs

    def get_all_job_names_with_url(self):
        r = self.jenkins.list_jobs()
        jobs = {_["name"]: _['url'] for _ in r.body['jobs']}
        '''
        创建一个一个叫jobs的字典对象，其中键是列表jobs中键为 'name 所对应的值作为新字典的键'
        其新字典所对应的值就是jobs列表中字典键为url 所对应的值
        '''
        return jobs

    # 封装更加简单的创建pipeline job的方法
    def create_job_with_dsl(self, dsl, job_name):
        r = self.jenkins.get_job(job_name)
        if r.code == 200:
            return "Fail:Job Aready Exist"

        script =f"""def jobDSL=\"\"\"{job_dsl}\"\"\";
                
            def flowDefinition=new org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition(jobDSL, true);
            def parent=Jenkins.instance;
            def job=new org.jenkinsci.plugins.workflow.job.WorkflowJob(parent,"job_created_by_http_method")
            job.definition=fowDefinition
            job.save();
            Jenkins.instance.reload()"""

        self.jenkins.run_groovy(script)
        r = self.jenkins.get_job(job_name)
        if r.code == 200 and r.body.get("displayName") == job_name:
            return f"OK:Job Create at {r.body.get('url')}"


# 2 封装httP 方法
# RestClient类的作用是用来代替Jenkins中的request session起到了精简代码的作用
# 同时也可以看成对rqeuests库做了二次开发：增加了打印url和拼接base_url的功能(知识点：只有在对功能做出修改后才会二次封装)
class RestClient():
    def __int__(self, base_url):
        self.base_url = base_url
        # 创建了一个reqests 的session
        self.s = requests.session()

    def get(self, endpoint, **kwargs):
        endpoint = self.base_url + endpoint
        print(f"GET url={endpoint}")
        r = self.s.get(endpoint, **kwargs)
        return self.process(r)

    def post(self, endpoint, data=None, json=None, **kwargs):
        endpoint = self.base_url + endpoint
        print(f"POST url={endpoint}")
        r = self.s.post(endpoint, data, json, **kwargs)
        return self.process(r)

    # 这个方法的的作用是把http响应进行解析，并且存到Response类里去
    def process(self, response):
        code = response.status_code
        try:
            body = response.json()
        except:
            body = str(response.content)
        return Response(code, body, response)


if __name__ == '__main__':
    # job_dsl中是一种描述性的语言是Jenkins2.0之后的一种类似于伪代码之类的东西这里是用来描述了一个pipeline job
    job_dsl = """properties([ 
                         parameters([
                            string(name:'Run',
                                   defaultValue:'Yes'
                                   description:'a parameter')
                                    ])
                    ])
     node {
       stage("test"){
         echo 'Hello world'
        }
    }"""
       # 远程执行groovy创建jenkins job
    admin = Jenkins("http://localhost:8080", "admin", "admin")
    # 调用封装好的业务方法
    r = admin.use_jenkins.create_job_with_dsl(job_dsl,"job_created_by_http_method")
    print(r)

    # 和没有优化相比，下面这这些代码都优化掉了
    # # 调用run groovy，创建job,名称为job_created_by_http_method
    # r = admin.run_groovy(script)
    # # 重新获取job,名称为job_created_by_http_method,返回的结果代码是200，并且获得了该job的一些配置信息
    # r = admin.get_job("job_created_by_http_method")
