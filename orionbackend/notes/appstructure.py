"""
# 1. Core App:
            Create a core app that contains shared functionality and models used in both modes.
            This app can include common models such as Player, Planet, Resource, etc. These models represent
            the fundamental entities of your game and can be used in both Rapid and Classical modes.


# 2. Rapid App:
            Create a separate app specifically for the Rapid mode. This app can include models, serializers,
            views, and other components specific to the Rapid mode. For example, you can have models like RapidPlayer,
            RapidPlanet, RapidTroop, etc., which inherit from the corresponding models in the core app. This approach
            allows you to extend the core models with mode-specific fields or behavior.

# 3. Classical App:
            Similar to the Rapid app, create a separate app for the Classical mode. It should contain models,
            serializers, views, and other components specific to the Classical mode. Use inheritance from the core app's
            models to add mode-specific fields or behavior. For example, you can have models like ClassicalPlayer,
            ClassicalPlanet, ClassicalTroop, etc.

# 4. Gameplay Logic:
            Consider creating a separate module or package that handles the gameplay logic shared between both
            modes. This module can contain functions or classes responsible for troop travel time calculations,
            construction speed, resource production rates, and other game-specific calculations. The gameplay logic can
            be accessed by the views in the Rapid and Classical apps as needed.
"""
