from typing import Any, TypeVar

from dacite import from_dict

T = TypeVar("T")

'''The convert_data_from_form_to_dto function is used to convert data from a form into an object of the DTO (Data Transfer Object) data type.

1. from typing import Any, TypeVar - imports Any and TypeVar types from the typing module.
2. from dacite import from_dict - imports the from_dict function from the dacite module. dacite is a library for converting dictionaries to object data.
3. T = TypeVar("T") - creates a TypeVar variable that can take any data type.
4. def convert_data_from_form_to_dto(dto: type[T], data_from_form: dict[str, Any]) -> Any: - definition of the convert_data_from_form_to_dto function with 
   two parameters: dto, which represents the DTO type, and data_from_form, which represents the data from the form in the form dictionary. The function returns 
   an object of type Any.
5. return from_dict(dto, data_from_form) - returns an object of type dto created from the data_from_form dictionary using the from_dict function from the dacite 
   library. The from_dict function converts data from a dictionary to an object of the given type, corresponding to the DTO.

So this function takes a DTO data type and a data dictionary from a form, and then converts that data into an object of the given DTO data type using 
dacite.from_dict(). It then returns this DTO for further processing in the application.'''

def convert_data_from_form_to_dto(dto: type[T], data_from_form: dict[str, Any]) -> Any:
    return from_dict(dto, data_from_form)
