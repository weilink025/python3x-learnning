#import导入模块时，是从path路径里搜索对应模块进行导入
from imp import *    #这个模块是可以重新载入模块的模块，但是快要被弃用了
import reload_moulde
reload_moulde.rel()

reload(reload_moulde)