from tethys_sdk.base import TethysAppBase, url_map_maker

"""
This app was developed by Riley Hales at Brigham Young University in December 2018
"""


class Analytics(TethysAppBase):
    """
    Tethys app class for Portal Analytics Viewer.
    """

    name = 'Portal Analytics Viewer'
    index = 'analytics:home'
    icon = 'analytics/images/analytics_icon.png'
    package = 'analytics'
    root_url = 'analytics'
    color = '#8b0000'
    description = 'View usage statistics as tracked by Google Analytics for configured apps on this portal'
    tags = 'Analytics'
    enable_feedback = True
    feedback_emails = []
    app_page = ''

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            # VIEWABLE PAGES
            UrlMap(
                name='home',
                url='analytics',
                controller='analytics.controllers.home'
            ),
            UrlMap(
                name='config',
                url='analytics/config',
                controller='analytics.controllers.config',
            ),
            UrlMap(
                name='requester',
                url='analytics/requester',
                controller='analytics.controllers.requester',
            ),
            UrlMap(                             # this is the controller for the page that shows app specific stats
                name='template',                # {name} is an argument the controller needs to accept second
                url='analytics/stats/{name}',
                controller='analytics.controllers.app_template'
            ),

            # AJAX CONTROLLERS
            UrlMap(
                name='get_app_list',
                url='analytics/ajax/get_applist',
                controller='analytics.ajaxhandlers.get_applist',
            ),
            UrlMap(
                name='app_stats',
                url='analytics/ajax/app_page',
                controller='analytics.ajaxhandlers.app_page',
            ),
            UrlMap(
                name='stats',
                url='analytics/ajax/requester',
                controller='analytics.ajaxhandlers.requester',
            ),
        )

        return url_maps
