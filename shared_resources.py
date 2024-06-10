from threading import Event, Lock

skills_active = Event()
skills_active.set()  # Allow typing initially

searching_active = Event()
searching_active.set()

typing_active = Event()
typing_active.set()

running = Event()

typing_lock = Lock()

mouse_lock = Lock()
