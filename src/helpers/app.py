def get_version_number(module) -> str:
    app = module.Application.get_application()  # get a handle to the App
    return f"{app.get_major_version()}.{app.get_minor_version()}.{app.get_bugfix_version()}"
