import web
import subprocess  

urls = (
    '/', 'index',
    '/test', 'index',
    '/rosweb', 'index'
)

class index:
    def GET(self):
        user_data = web.input()
        if user_data.id == '11': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/mini-start-bg.sh")   
        elif user_data.id == '10': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/mini-stop.sh") 
        elif user_data.id == '21': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/mini-imu-start-bg.sh")   
        elif user_data.id == '20': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/mini-imu-stop.sh") 
        elif user_data.id == '101': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/gmapping-start-bg.sh") 
        elif user_data.id == '100': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/gmapping-stop.sh") 
        elif user_data.id == '102': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/gmapping-save.sh " + user_data.name) 
        elif user_data.id == '111': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/gmapping-imu-start-bg.sh") 
        elif user_data.id == '110': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/gmapping-imu-stop.sh") 
        elif user_data.id == '112': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/gmapping-imu-save.sh " + user_data.name)
        elif user_data.id == '201': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/navigation-start-bg.sh") 
        elif user_data.id == '200': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/navigation-stop.sh")  
        elif user_data.id == '211': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/navigation-imu-start-bg.sh") 
        elif user_data.id == '210': 
            return subprocess.getoutput("/home/eaibot/dashgo_ws/src/dashgo/dashgo_tools/startup/navigation-imu-stop.sh") 
        else:
            return "other!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
