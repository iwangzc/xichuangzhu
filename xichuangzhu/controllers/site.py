# coding: utf-8
from flask import render_template, Blueprint
from ..models import db, Work, WorkImage, WorkReview, Author, Dynasty

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    """首页"""
    works = Work.query.order_by(db.func.random()).limit(4)
    work_images = WorkImage.query.order_by(WorkImage.create_time.desc()).limit(18)
    work_reviews = WorkReview.query.filter(WorkReview.is_publish).order_by(
        WorkReview.create_time.desc()).limit(4)
    authors = Author.query.order_by(db.func.random()).limit(5)
    dynasties = Dynasty.query.order_by(Dynasty.start_year.asc())
    return render_template('site/index.html', works=works, work_images=work_images,
                           work_reviews=work_reviews, authors=authors, dynasties=dynasties)


@bp.route('/works', methods=['POST'])
def works():
    """生成首页需要的作品json数据"""
    works = Work.query.order_by(db.func.random()).limit(4)
    return render_template('macro/index_works.html', works=works)


@bp.route('/about')
def about():
    """关于页"""
    return render_template('site/about.html')


@bp.route('/disclaimer')
def disclaimer():
    """免责声明"""
    return render_template('site/disclaimer.html')


@bp.route('/update')
def update():
    """Just for benchmark vs Node.js"""
    import json
    from ..models import Work

    result = []
    for work in Work.query.filter(Work.highlight):
        result.append({
            'id': work.id,
            'update_at': work.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return json.dumps(result)