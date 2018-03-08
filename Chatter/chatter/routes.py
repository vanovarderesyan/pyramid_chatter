def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=0)
    config.add_route('send', '/send')
    config.add_route('home', '/')
