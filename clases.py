import unittest
class Materia:
    def __init__(self, nombre, profesores,alumno):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumno__ = alumno

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumno(self):
        return self.__alumno__

class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__
#OBJETOS   
profesor= Profesor(nombre="Daniel",cargo="Titular",legajo="123")



class Alumno:
    def __init__(self,nombre,año,carrera):
     self.__nombre__= nombre
     self.__año__= año
     self.__carrera__ = carrera
     self.__mentor__ = None

    def obtener_alumnos(self):
        return self.__nombre__ 
    
    def agregar_mentor(self,mentor):
        self.__mentor__ = mentor
    
#OBJETOS
camila = Alumno(nombre="Camila",año="2do",carrera="Informatica")
valentina =Alumno(nombre="Valentina",año="2do",carrera="Bioingenieria")



class TestMateria(unittest.TestCase):

    def test_materia(self):
        materia_1= Materia(nombre="Matematica",profesores=["Daniel","Walter"],alumno=["Camila","Valentina"])
        self.assertEqual(materia_1.__nombre__,"Matematica")
        self.assertEqual(materia_1.__profesores__,["Daniel","Walter"])
        self.assertEqual(materia_1.__alumno__,["Camila","Valentina"])

    def test_obtener_profesores(self):
        profes_materia = Materia(nombre=None,profesores=["Daniel","Walter"],alumno=None)
        self.assertEqual(profes_materia.__profesores__,["Daniel","Walter"])

    def test_cambiar_nombre(self):
        materia_1 = Materia(nombre="Matematica",profesores=None,alumno=None)
        materia_1.cambiar_nombre("Calculo")
        self.assertEqual(materia_1.__nombre__,"Calculo")
    
    def test_obtener_alumnos(self):
        alumnos=Materia(nombre=None,profesores=None,alumno=["Camila","Valentina"])
        self.assertEqual(alumnos.__alumno__,["Camila","Valentina"])

class TestPorfesor(unittest.TestCase):

    def test_profesor(self):
        profe = Profesor(nombre="Daniel", cargo="Titular",legajo="123")
        self.assertEqual(profe.__nombre__,"Daniel")
        self.assertEqual(profe.__cargo__,"Titular")
        self.assertEqual(profe.__legajo__,"123")

    def test_obtener_nombre(self):
        profe = Profesor(nombre="Daniel",cargo=None,legajo=None)
        self.assertEqual(profe.__nombre__,"Daniel")

    def test_obtener_legajo(self):
        profe = Profesor(nombre=None,cargo=None,legajo="123")
        self.assertEqual(profe.__legajo__,"123")

    def test_obtener_cargo(self):
        profe = Profesor(nombre=None,cargo="Titular",legajo=None)
        self.assertEqual(profe.__cargo__,"Titular")

class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno= Alumno(nombre="Camila",carrera="Informatica",año="2do")
        self.assertEqual(alumno.__nombre__,"Camila")
        self.assertEqual(alumno.__carrera__,"Informatica")
        self.assertEqual(alumno.__año__,"2do")

    def test_obtener_alumnos(self):
        alumnos=Alumno(nombre="Camila",carrera=None,año=None)
        self.assertEqual(alumnos.__nombre__,"Camila")

    def test_agregar_mentor(self):
        alumno= Alumno(nombre=None,carrera=None,año=None)
        alumno.agregar_mentor("Carlos")
        self.assertEqual(alumno.__mentor__,"Carlos")






   

unittest.main()

