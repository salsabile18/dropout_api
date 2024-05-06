from pydantic import BaseModel

class DropoutData(BaseModel):
    id_typeEnseignement:      str
    NbrRedoublement :         str
    MoyenneNotes :            str
    Exclus       :            str
    id_Genre     :            str
    Age          :            str
    CD_REG       :            str
    cd_com       :            str
    CD_MIL       :            str
    suffix_index :            str