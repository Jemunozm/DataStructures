from BSTEntry import BSTEntry

materiales = BSTEntry("llave",10)

print(materiales.getData())
print(materiales.getKey())

materiales.setData("caja")
materiales.setKey(100)

print(materiales.getData())
print(materiales.getKey())