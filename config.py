# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'tuscaloosa',
    package_name = 'montclair-tuscaloosa',
    name = 'Go Tuscaloosa',
    description = 'Real Time Tracking of the Buses for Tuscaloosa, AL',
    url = 'https://tuscaloosa.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.12.0',
        revision = 1,
        title = 'Go Tuscaloosa',
        first_run_text = "Welcome to Tuscaloosa, AL's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.tuscaloosa',
        app_store_id = '1495548625',
        app_store_url = 'https://apps.apple.com/us/app/go-tuscaloosa/id1495548625'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.2.0',
        revision = 1,
        app_id = 'com.gotransitapp.tuscaloosa',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.tuscaloosa'
    )
)
