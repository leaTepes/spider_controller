from celery.task import task
from celery import Celery

from dynamic_scraper.utils.task_utils import TaskUtils
from search_results.models import NewsWebsite, Article


app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def run_spiders():
    t = TaskUtils()
    t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider')


@app.task
def run_checkers():
    t = TaskUtils()
    t.run_checkers(Article, 'news_website__scraper', 'checker_runtime', 'article_checker')