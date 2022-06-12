*** Settings ***
Library    ..\\recommender\\Day.py    ${date}    ${description}    ${warmest}    ${windspeed}    ${rainfall}    ${location}    WITH NAME    day1
Library    ..\\recommender\\Day.py    ${date2}    ${description2}    ${warmest2}    ${windspeed2}    ${rainfall2}    ${location2}    WITH NAME    day2
Library    ..\\recommender\\Day.py    ${date3}    ${description3}    ${warmest3}    ${windspeed3}    ${rainfall3}    ${location3}    WITH NAME    day3
Library    ..\\recommender\\Day.py    ${date4}    ${description4}    ${warmest4}    ${windspeed4}    ${rainfall4}    ${location4}    WITH NAME    day4
Library    ..\\recommender\\day_evaluator.py    WITH NAME    DayEvaluator
Library    Collections

*** Test Cases ***
Get all days that are fair
    @{instances}    Get list as instances    @{day_list}
    @{fairs}=    Get fair days    @{instances}
    @{corrects}=    Get list as instances    ${day1}    ${day4}
    Check list contains values    ${corrects}    ${fairs}

Get all days that are clear
    @{instances}    Get list as instances    @{day_list}
    @{clears}=    Get clear days    @{instances}    
    @{corrects}=    Get list as instances    ${day1}    ${day2}
    Check list contains values    ${corrects}    ${clears}

Get all half cloudy days
    @{instances}    Get list as instances    @{day_list}
    @{half_cloudys}=    Get half cloudy days    @{instances}
    ${day_three}    Get library instance    ${day3}
    List Should Contain Value    ${half_cloudys}    ${day_three}

Get day with best temperature
    @{instances}    Get list as instances    @{day_list}
    ${best_day}=    Get best temperature day    ${19}    @{instances}    
    ${day_two}    Get library instance    ${day2}
    Should Be Equal    ${best_day}    ${day_two}

Get days that are not too windy
    @{instances}    Get list as instances    @{day_list}
    @{not_windy}=    Get not windy days    @{instances}
    ${day_four}=    Get library instance    ${day4}
    List Should Not Contain Value    ${not_windy}    ${day_four}

*** Keywords ***
Get fair days
    [Arguments]    @{days}
    @{fair_days}=    DayEvaluator.fairDays    ${days}
    RETURN    @{fair_days}    

Get clear days
    [Arguments]    @{days}
    @{clear_days}=    DayEvaluator.clearDays    ${days}
    RETURN    @{clear_days}

Get half cloudy days
    [Arguments]    @{days}
    @{half_cloudy_days}=    DayEvaluator.halfCloudyDays    ${days}
    RETURN    @{half_cloudy_days}

Get best temperature day
    [Arguments]    ${maxtemp}    @{days}    
    ${best}=    DayEvaluator.dayWithBestTemp    ${days}    ${maxtemp}
    RETURN    ${best}

Get not windy days
    [Arguments]    ${maxwind}    @{days}
    @{not_too_windy}=    DayEvaluator.removeWindyDays    ${days}    ${maxwind}
    RETURN    @{not_too_windy}

Get list as instances
    [Arguments]    @{list}
    @{instances}    Create List
    FOR    ${item}    IN    @{list}
        ${listitem}=    Get library instance    ${item}
        Append To List    ${instances}    ${listitem}   
    END 
    RETURN    @{instances} 

Check list contains values
    [Arguments]    ${values}    @{list}
    FOR    ${value}    IN    ${values}
        List Should Contain Value    ${list}    ${value}
    END

*** Variables ***
${day1}    day1
${day2}    day2
${day3}    day3
${day4}    day4
@{day_list}    ${day1}    ${day2}    ${day3}    ${day4}
${date}    12.06.2022
${description}    Poutaa ja selkeää
${warmest}    +31
${windspeed}    4
${rainfall}    0
${location}    Vantaa
${date2}    13.06.2022
${description2}    Melkein selkeää
${warmest2}    +19
${windspeed2}    5
${rainfall2}    0.1
${location2}    Vantaa
${date3}    14.06.2022
${description3}    Puolipilvistä
${warmest3}    +18
${windspeed3}    6
${rainfall3}    0.2
${location3}    Vantaa
${date4}    15.06.2022
${description4}    Pilvistä ja Poutaa
${warmest4}    +17
${windspeed4}    20
${rainfall4}    0.3
${location4}    Vantaa