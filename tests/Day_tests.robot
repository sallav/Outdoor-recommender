*** Settings ***
Library    ..\\recommender\\Day.py    ${date}    ${description}    ${warmest}    ${windspeed}    ${rainfall}    ${location}    WITH NAME    day1
Library    ..\\recommender\\Day.py    ${date2}    ${description2}    ${warmest2}    ${windspeed2}    ${rainfall2}    ${location2}    WITH NAME    day2

*** Test Cases ***
Day is warmer
    ${result}=    Is day warmest    ${day1}    ${day2}
    Should Be True    ${result}  

Day is clear 
    ${result}=    Is day clear    ${day1}
    Should Be True    ${result}  

Day is fair
    ${result}=    Is day fair    ${day1}
    Should Be True    ${result}

Day is not half cloudy
    ${result}=     Is day half cloudy    ${day1}
    Should Not Be True    ${result}

Get day ratings
    ${first}=    Get rating    ${day1}
    ${second}=    Get rating    ${day2}
    Should Be True    ${first} > ${second}

Prind day details
    ${result}=    Print day    ${day1} 
    Should Contain    ${result}    ${date}    
    Should Contain    ${result}    ${description}    
    Should Contain    ${result}    ${warmest} 
    Should Contain    ${result}    ${windspeed} 
    Should Contain    ${result}    ${rainfall}    
    Should Contain    ${result}    ${location}

*** Keywords ***
Is day warmest
    [Arguments]    ${first}    ${second}
    ${fday}=    Get library instance    ${first}
    ${sday}=    Get library instance    ${second}
    ${value}=    call method    ${fday}    warmer    ${sday}
    RETURN    ${value}

Is day clear
    [Arguments]    ${obj}
    ${day}=    Get library instance    ${obj}
    ${result}=    call method    ${day}    clear
    RETURN    ${result}

Is day fair
    [Arguments]    ${obj}
    ${day}=    Get library instance    ${obj}
    ${result}=    call method    ${day}    fair
    RETURN    ${result}

Is day half cloudy
    [Arguments]    ${obj}
    ${day}=    Get library instance    ${obj}
    ${result}=    call method    ${day}    halfCloudy
    RETURN    ${result}

Get rating
    [Arguments]    ${obj}
    ${day}=    Get library instance    ${obj}
    call method    ${day}    rate
    ${result}=    call method    ${day}    getRating  
    RETURN    ${result}

Print day
    [Arguments]    ${obj}
    ${day}=    Get library instance    ${obj}
    ${result}=    call method    ${day}    toString
    RETURN    ${result}

*** Variables ***
${day1}    day1
${day2}    day2
${date}    11.06.2022
${description}    Poutaa ja selkeää
${warmest}    +20
${windspeed}    5
${rainfall}    0
${location}    Vantaa
${date2}    12.06.2022
${description2}    Melkein selkeää
${warmest2}    +18
${windspeed2}    4
${rainfall2}    1
${location2}    Helsinki 