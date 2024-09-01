from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath
from direct.task import Task

class Game(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
        
        # Завантажуємо модель
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
        
        # Створюємо NodePath для камери і переміщуємо його в потрібне положення
        self.camera_node = NodePath('camera_node')
        self.camera_node.reparentTo(render)
        self.camera_node.setPos(0, -30, 10)  # Встановлюємо камеру позаду об'єкта
        
        # Прив'язуємо камеру до camera_node
        self.camera.reparentTo(self.camera_node)
        
        # Налаштовуємо події клавіатури
        self.accept('arrow_left', self.start_rotate_left)
        self.accept('arrow_right', self.start_rotate_right)
        self.accept('arrow_up', self.start_move_forward)
        self.accept('arrow_down', self.start_move_backward)
        
        self.accept('arrow_left-up', self.stop_rotate)
        self.accept('arrow_right-up', self.stop_rotate)
        self.accept('arrow_up-up', self.stop_move)
        self.accept('arrow_down-up', self.stop_move)
        
        self.rotation_speed = 3.0  # Швидкість обертання камери
        self.movement_speed = 10.0  # Швидкість переміщення камери
        
        self.rotate_left = False
        self.rotate_right = False
        self.move_forward = False
        self.move_backward = False
        
        # Додаємо задачу для оновлення позиції камери
        self.taskMgr.add(self.update_camera_task, "update_camera_task")
    
    def start_rotate_left(self):
        self.rotate_left = True
    
    def start_rotate_right(self):
        self.rotate_right = True
    
    def start_move_forward(self):
        self.move_forward = True
    
    def start_move_backward(self):
        self.move_backward = True
    
    def stop_rotate(self):
        self.rotate_left = False
        self.rotate_right = False
    
    def stop_move(self):
        self.move_forward = False
        self.move_backward = False
    
    def update_camera_task(self, task):
        if self.rotate_left:
            self.camera_node.setH(self.camera_node.getH() + self.rotation_speed)
        
        if self.rotate_right:
            self.camera_node.setH(self.camera_node.getH() - self.rotation_speed)
        
        if self.move_forward:
            self.camera_node.setPos(self.camera_node.getPos() + self.camera_node.getQuat().getForward() * self.movement_speed)
        
        if self.move_backward:
            self.camera_node.setPos(self.camera_node.getPos() - self.camera_node.getQuat().getForward() * self.movement_speed)
        
        return Task.cont

game = Game()
game.run()
