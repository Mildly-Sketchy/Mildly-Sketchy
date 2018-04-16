def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/auth')
    # config.add_route('register', '/auth')
    config.add_route('logout', '/logout')
    config.add_route('profile', '/profile')
    config.add_route('analytics', '/analytics')
    config.add_route('about', '/about')
    config.add_route('email', '/email')
