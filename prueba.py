import pydicom
import matplotlib.pyplot as plt

# Ruta a tu archivo DICOM
path = r"C:\Users\alfon\OneDrive\Documentos\IBERO\INTERNADO\PRE-ESTUDIO\PYTHON/1-1.dcm"

# Leer el archivo
dicom_img = pydicom.dcmread(path)

# Mostrar la imagen
plt.imshow(dicom_img.pixel_array, cmap='gray')
plt.title(dicom_img.SeriesDescription)
plt.show()
