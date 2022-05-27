artist = "Tage Åsén" 
print(artist.encode("Latin1")) 
print(artist.encode("CP850")) 
print(artist.encode("utf8")) 
print(artist.encode("utf16")) 

print(artist.encode("ascii", 'ignore'))
print(artist.encode("ascii", 'replace'))
print(artist.encode("ascii", 'backslashreplace'))
print('{!a}'.format(artist))

print(b'Tage \xc3\x85s\xc3\xa9n'.decode("utf8"))
