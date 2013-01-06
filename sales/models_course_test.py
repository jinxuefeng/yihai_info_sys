# -*- coding:utf-8 -*-
from django.db import models

# Category
class Category(models.Model):
    "Categery of Courses, hierarchical structure." 

    #root Category has parent_id as null
    parent_id = models.ForeignKey('self', null=True)
    #name length here and in other Models need to be set, say 100 now
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name
# Course
class Course(models.Model):
    "Course, must belong to a specific Category"

    COURSE_STATUS_CHOICES = (
        (u'uncert',      u'uncertified'),
        (u'free',        u'free'),
        (u'open',        u'open'),
        (u'hide',        u'hide'),
    )

    COURSE_LEVEL_CHOICES = (
        (u'easy',    u'easy'),
        (u'hard',    u'hard'),
        (u'pro',     u'professional'),
    )

    COURSE_FLAGS_CHOICES = (
        (u'new',    u'new'),
        (u'sel',   u'selected'),
        (u'hot',    u'bot'),
    )

    COURSE_MEDIA_CHOICES = (
        (u'static',    u'text and picture'),
        (u'video',     u'video'),
    )

    name = models.CharField(max_length = 100)
    descption = models.TextField()
    section_num = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    #所有者ID, Gikoo平台or各企业客户
    owner_id = models.IntegerField()
    #课程学分
    credit = models.PositiveIntegerField()
    #课程状态 1：未审核、2：免费、3：开放、4：隐藏
    status = models.CharField(max_length=10, choices=COURSE_STATUS_CHOICES)
    #课程总点击数
    click_num = models.PositiveIntegerField(default=0)
    #FK, connect to a Category
    category_id = models.ForeignKey(Category)
    #thumbnail地址
    thumbnail_url = models.URLField()
    #课程封面(大)地址
    thumbnail_url = models.URLField()
    #课程封面(小)地址
    thumbnail_url = models.URLField()
    #课程下架时间
    end_time = models.DateTimeField()
    #课程推荐学习时限 类型是否合适??
    recommend_duration = models.PositiveIntegerField()
    #课程难易程度 分几级??
    level = models.CharField(max_length=10, choices=COURSE_LEVEL_CHOICES)
    #课程地址
    url = models.URLField()
    #课程种类 图文or视频
    media_type = models.CharField(max_length=10, choices=COURSE_MEDIA_CHOICES)
    #文件名称 是否冗余?? 
    filename = models.CharField(max_length=100, blank=True)
    #课程flag 1：最新课程，2：精品课程，4：热闹课程
    flag = models.CharField(max_length=10, choices=COURSE_FLAGS_CHOICES, blank=True)  

    def __unicode__(self):
        return self.name

#Rating
class Rating(models.Model):
    "course ratings"

    course_id = models.ForeignKey(Course)
    user_id = models.IntegerField()
    #rating 有没有固定分级?
    rate = models.IntegerField()
    title = models.CharField(max_length = 100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

#Section in a Course
class Section(models.Model):
    "section in a course"

    title = models.CharField(max_length = 100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    course_id = models.ForeignKey(Course)
    click_number = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

#course tag
class CourseTag(models.Model):
    "CourseTag, used to feature a Course"

    course_id = models.ForeignKey(Course)
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name


#question pool
class QuestionPool(models.Model):
    "collection of a bunch of questions for quiz or survey"
    
    #题库分为两种 考试(test)和调查(survey)
    QUESTIONPOOL_TYPES_CHOICES = (
        (u'test', u'test'),
        (u'surv', u'survey'),
    )

    course_id = models.ForeignKey(Course)
    category_id = models.ForeignKey(Category)
    pool_type = models.CharField(max_length=10, choices=QUESTIONPOOL_TYPES_CHOICES)

#Question
class Question(models.Model):
    "question"

    QUESTION_TYPE__CHOICES = (
        (u'single',    u'single choice'),
        (u'multi',     u'multiple choice'),
    )
    question = models.TextField()
    #how to store this picture?
    image = models.ImageField(upload_to='gikoo/question', blank=True)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPE__CHOICES)
    #max_length=?
    answer = models.CharField(max_length=5)
    ative = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)
    question_pool_id = models.ForeignKey(QuestionPool)

#AnswerCandidate
class AnswerCandidate(models.Model):
    "an canditate answer to a specific question"

    question_id = models.ForeignKey(Question)
    #备选答案顺序?
    order = models.PositiveIntegerField(default=0)
    candidate = models.CharField(max_length=5)
    image = models.ImageField(upload_to='gikoo/question', blank=True)

#Quiz
class Quiz(models.Model):
    "a quiz generated from a specific question pool"


    QUIZ_TYPES_CHOICES = (
        (u'test', u'test'),
        (u'surv', u'survey'),
    )
    name = models.CharField(max_length=100)
    question_pool_id = models.ForeignKey(QuestionPool)
    #考试时间，可选项
    time_limit = models.PositiveIntegerField(blank=True)
    #学员最多可以参加的考试次数??
    max_times = models.PositiveIntegerField()
    #默认不可见答案
    show_answer = models.BooleanField(default=False)
    passmark = models.PositiveIntegerField()
    question_number = models.PositiveIntegerField()
    #单选还是多选
    quiz_type = models.CharField(max_length=10, choices=QUIZ_TYPES_CHOICES)
    active = models.BooleanField(default=False)
    

    def __unicode__(self):
        return self.name

#QuizPrecondition
class QuizPrecondition(models.Model):
    "fullfilled the requirement can you take the related quiz"
    
    quiz_id = models.ForeignKey(Quiz)
    course_id = models.ForeignKey(Course)
    section_id = models.ForeignKey(Section)

#QuizResult
class QuizResult(models.Model):
    "result of a quiz"

    #Usr model not realized
    user_id = models.ForeignKey('User')
    quiz_id = models.ForeignKey(Quiz)
    score = models.PositiveIntegerField(default=0)
    #time used by tester?
    time = models.PositiveIntegerField(default=0)

#QuizResultDetail
class QuizResultDetail(models.Model):
    "see answer of a question"

    question_id = models.ForeignKey(Question)
    #用户做的答案
    answer = models.CharField(max_length=5)
    quiz_result_id = models.ForeignKey(QuizResult)

    






