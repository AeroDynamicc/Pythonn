

# Küsi kasutajalt faili nime
$fileName = Read-Host "Sisesta csv fail"

# Kontrolli kas tegu on csv failiga
if($fileName -notmatch ".csv") {
    Write-Host "Error: Palun sisestage csv fail"
    return
}

# Palub kasutajal sisestada domeeninime
$domain = Read-Host "Sisesta doomeninimi (ex. domain.com)"

# Loen kasutajanime csv failist
$users = Import-Csv $fileName

# Sirvida läbi iga kasutaja ja teisendada nende nimi e-posti aadressiks
foreach($user in $users) {
    # Saada eesnime ja perenime
    $firstName = $user.FirstName
    $lastName = $user.LastName

    # Teisendage ees- ja perekonnanimi väiketähtedeks
    $firstName = $firstName.ToLower()
    $lastName = $lastName.ToLower()

    # Looge emaili kasutaja/konto
    $123.txt = "$firstName.$lastName@$domain"

    # Prindi email aadress
    Write-Host $email
}

# Salvesta meiliaadressid tekstifaili
$email | Out-File "123.txt"































