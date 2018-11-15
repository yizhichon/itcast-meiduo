from celery import Celery
from .config import broker_url,result_backend


# 为celery使用django配置文件进行设置
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'


celery_app = Celery('meiduo',broker=broker_url,backend=result_backend)

# 对celery应用添加配置信息
# celery_app.config_from_object("celery_tasks.config") # win不支持

celery_app.autodiscover_tasks(["celery_tasks.sms","celery_tasks.emails"]) # 以目录形式定义,py文件为tasks会自动搜寻


# 开启celery的命令
#  celery -A 应用路径（.包路径） worker -l info
#  celery -A celery_tasks.main worker -l info