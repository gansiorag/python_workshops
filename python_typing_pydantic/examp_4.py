# Monitoring Pydantic with Logfire
from datetime import datetime
from typing import (Text, Any, Union, 
                    List, Dict, Tuple, 
                    Set, Optional)
import logfire

from pydantic import BaseModel

logfire.configure()
logfire.instrument_pydantic()  

class Adress(BaseModel):
    index: Optional[Text] = None
    city: Optional[Text] = None
    dom: Optional[List| Dict] = None

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]



# this will record details of a successful validation to logfire
m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)

Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '21'])

add = Adress(index = '2356347', dom = {'street': 'Lenina', 'number': 23})

print(add)
