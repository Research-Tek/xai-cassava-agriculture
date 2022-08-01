SWRL_RULES = {
    "cbb": {
        "rainy_season": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isPartOfField(?soil, ?field),
            hasRainySeason(?field, ?rainy),
            equal(?rainy, true),
            -> hasCondition(?plant, CBBRainySeason)""",

        "soil_moisture": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilMoisture),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 0.3),
            -> hasCondition(?plant, CBBSoilMoisture)""",

        "soil_ph": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilPH),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 6.5),
            lessThanOrEqual(?result, 7.2),
            -> hasCondition(?plant, CBBSoilPH)""",

        "soil_temperature": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilTemperature),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 25),
            lessThanOrEqual(?result, 30),
            -> hasCondition(?plant, CBBSoilTemperature)"""
    },
    "cbsd": {
        "humidity": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isPartOfField(?soil, ?field),
            isFeatureOfInterestOf(?field, ?obs),
            observedProperty(?obs, RelativeHumidity),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 0.7),
            lessThanOrEqual(?result, 0.85),
            -> hasCondition(?plant, CBSDRelativeHumidity)""",
        "soil_moisture": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilMoisture),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 0.1),
            -> hasCondition(?plant, CBSDSoilMoisture)""",
        "soil_temperature": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilTemperature),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 10),
            lessThanOrEqual(?result, 32),
            -> hasCondition(?plant, CBSDSoilTemperature)"""
    },
    "cgm": {
        "soil_moisture": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilMoisture),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 0.7),
            -> hasCondition(?plant, CGMSoilMoisture)""",
        "humidity": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isPartOfField(?soil, ?field),
            isFeatureOfInterestOf(?field, ?obs),
            observedProperty(?obs, RelativeHumidity),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 0.7),
            -> hasCondition(?plant, CGMRelativeHumidity)""",
        "soil_temperature": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilTemperature),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 27),
            -> hasCondition(?plant, CGMSoilTemperature)"""
    },
    "cmd": {
        "temperature": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isPartOfField(?soil, ?field),
            isFeatureOfInterestOf(?field, ?obs),
            observedProperty(?obs, Temperature),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 30),
            -> hasCondition(?plant, CMDTemperature)""",
        "soil_moisture": """
           Plant(?plant),
           isPlantedIn(?plant, ?soil),
           isFeatureOfInterestOf(?soil, ?obs),
           observedProperty(?obs, SoilMoisture),
           hasSimpleResult(?obs, ?result),
           greaterThanOrEqual(?result, 0.3),
           -> hasCondition(?plant, CMDSoilMoisture)""",
        "soil_temperature": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isFeatureOfInterestOf(?soil, ?obs),
            observedProperty(?obs, SoilTemperature),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 20),
            lessThanOrEqual(?result, 32),
            -> hasCondition(?plant, CMDSoilTemperature)""",
        "humidity": """
            Plant(?plant),
            isPlantedIn(?plant, ?soil),
            isPartOfField(?soil, ?field),
            isFeatureOfInterestOf(?field, ?obs),
            observedProperty(?obs, RelativeHumidity),
            hasSimpleResult(?obs, ?result),
            greaterThanOrEqual(?result, 0.8),
            -> hasCondition(?plant, CMDHighRainfall)"""
    },

}
