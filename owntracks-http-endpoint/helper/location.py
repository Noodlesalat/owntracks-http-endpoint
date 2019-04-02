class Location():
    # accuracy - Genauigkeit
    # altitude - Höhe
    # battery - Akkustand
    # connection - w -> phone is connected to a WiFi connection (iOS,Android); 
    #   o -> phone is offline (iOS,Android), m -> mobile data (iOS,Android)
    # latitude - Breitengrad
    # longitude - Längengrad
    # trigger - p -> ping issued randomly by background task (iOS,Android)
    #   c -> circular region enter/leave event (iOS,Android)
    #   b -> beacon region enter/leave event (iOS)
    #   r -> response to a reportLocation cmd message (iOS,Android)
    #   u -> manual publish requested by the user (iOS,Android)
    #   t -> timer based publish in move move (iOS)
    #   v -> updated by Settings/Privacy/Locations Services/System Services/Frequent Locations monitoring (iOS)
    # trackerID - Tracker Identifiaction
    # timestamp - Publish Timestamp
    # velocity - Geschwindigkeit
    __slots__ = ['accuracy', 'altitude', 'battery', 'connection', 'latitude', 'longitude', 'trigger', 'trackerID', 'timestamp', 'velocity']