# -*- coding: utf-8 -*-

from anwen.index import IndexHandler, WelcomeHandler, ExploreHandler
from anwen.index import RecommendedHandler, CollectionsHandler
from anwen.index import NodeHandler, TagHandler

from anwen.user import LoginHandler, JoinusHandler, LogoutHandler
from anwen.user import GoogleLoginHandler
from anwen.user import ForgotPassHandler, SetPassHandler
from anwen.user import SettingHandler, ChangePassHandler
from anwen.user import UserhomeHandler, UserlikeHandler
from anwen.user import UsersHandler

from anwen.share import ShareHandler, EntryHandler, CommentHandler, LikeHandler
from anwen.share import FeedHandler
from anwen.share import ImageUploadHandler
from anwen.share import SharesHandler, CommentsHandler

from anwen.other import EditHandler, ErrHandler, FeedbackHandler, ScoreHandler


handlers = [
    (r"/welcome", WelcomeHandler),
    (r"/explore", ExploreHandler),
    (r"/", IndexHandler),
    (r"/recommended", RecommendedHandler),
    (r"/collections", CollectionsHandler),

    (r"/node/([^/]+)", NodeHandler),
    (r"/tag/?", TagHandler),
    (r"/tag/([^/]+)", TagHandler),

    (r"/login", LoginHandler),
    (r"/joinus", JoinusHandler),
    (r"/logout", LogoutHandler),
    (r"/google_login", GoogleLoginHandler),
    (r'/forgotpass', ForgotPassHandler),
    (r'/setpass', SetPassHandler),
    (r'/setting', SettingHandler),
    (r'/changepass', ChangePassHandler),
    (r"/user/([^/]+)", UserhomeHandler),
    (r"/userlike/([^/]+)", UserlikeHandler),
    (r"/users/?", UsersHandler),
    (r'/users/([0-9a-f]{24})', UsersHandler),

    (r"/share/?", ShareHandler),
    (r"/share/([^/]+)", EntryHandler),
    (r"/sharecomment", CommentHandler),
    (r"/sharelike/([^/]+)", LikeHandler),
    (r"/share/image_upload", ImageUploadHandler),
    (r"/feed", FeedHandler),

    (r"/shares/?", SharesHandler),
    (r"/shares/([0-9a-f]{24})", SharesHandler),
    (r"/comments/?", CommentsHandler),
    (r"/comments/([0-9a-f]{24})", CommentsHandler),

    (r"/score/([^/]+)", ScoreHandler),
    (r"/feedback", FeedbackHandler),
    (r"/edit", EditHandler),
    (r'/404', ErrHandler),

    (r'/(.*)', EntryHandler),
    # Custom 404 ErrHandler, always put this at last

]
