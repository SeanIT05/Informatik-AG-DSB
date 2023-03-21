# OS bauen mithilfe von Archlinux
![alt text](https://github.com/archlinux/.github/raw/main/profile/archlinux-logo-dark-scalable.svg)
# So mache ICH es gerne..

Heißt nicht, dass es so sein muss...
# Vor der Installation

- Software runterladen um ISO auf einen USB Stick brennen zu können...
- Ein positives Mindset haben.
- Auf 99% von euren Computern wird es funktionieren.
- Lernen was man eigentlich eingibt.
- [Installations-Guide folgen](https://wiki.archlinux.org/title/Installation_guide) (Das meiste hier bezieht sich nicht auf uns)
- Have fun!
# Anfang der Installation

```
loadkeys de    (Deine PC Keymap/Tastatursprache)
ping gnu.org
```
*ctrl+c* (um mit dem Ping aufzuhören)
```
timedatectl set-ntp true
```
Systemuhr einstellen
# Disk aufteilen

```
wipefs -a /dev/YOURDEVICE 

DAS WIRD DEIN DRIVE LÖSCHEN. BITTE PASS AUF, DASS DU ALLES GESPEICHERT HAST.
ICH WERDE KEINE KOSTEN DAFÜR TRAGEN!
```
---
```
fdisk -l
fdisk /dev/YOURDRIVE
```
Jetzt befindest du dich in Fdisk. [^1] 

### Aufteilung der 1. Partition

```
m     (print help menu)
g     (GPT Partition Table)
n     (New Partition)
1     (Erste Partition)
enter (Anfang der Partition)
+550M (Größe der EFI Partition)
(Ende der 1. Partition)
```
Was bedeutet "M"? [^2]

### Aufteilung der 2. Partition

```
n
2
enter    (Der Sektor wird automatisch am Ende des 1. anfangen)
+8G      (Lese dir unten meinen Guide zu Swap vor)
Ende der 2. Partition
```
### Wie viel Swap?

Hier wird wieder meine Meinung reflektiert, aber viele Menschen würden hiermit zustimmen.

![](https://i.imgur.com/21FIr8Y.png)
### Aufteilung der 3. Partition

```
n
3
enter
enter        (So sagen wir fdisk, dass wir den Rest geben wollen.
              Wie man sieht ist das hier die größte Partition.
              Unsere sogenannte "Root Partition", wo sich unsere
              Software, Images und alles befindet...)
```
### "Type" ändern

Hier ändern wir die Art der Partition, damit unser System weiss, wozu sie dient.

(Wir befinden uns noch in fdisk)
```
t    (Type ändern)
1    (1. Partition)
L    (Types anzeigen)--> "q" um aus dem Menu zu kommen.
1    (EFI sollte das 1. sein. Bitte nachschauen!)

t    
2
L
19   (Linux Swap. Bitte nachschauen!)

Die 3. muss man nicht ändern

w    (Änderungen speichern!!!)
```
Wieso muss ich die 3. nicht ändern?[^3]

# File System generieren

Hier musst du den 3 verschiedenen Partitions "Filesystems zuordnen"...

```
mkfs.fat -F32 /dev/YOURDEVICE1

mkswap        /dev/YOURDEVICE1    (Swap System machen)

swapon        /dev/YOURDEVICE2    (Swap aktivieren. Aktiviere das in der gleichen
                           Partition, wo du "mkswap" gemacht hast.)
mkfs.ext4     /dev/YOURDEVICE3
```
# File Systeme "mounten"

Hier sagen wir unserem System, wo diese Filesysteme "gemountet" werden sollen.

```
mount /dev/YOURDEVICE3 /mnt    ( /mnt steht für "mount")

pacstrap /mnt base linux linux-firmware
```
Mit ["pacstrap"](https://man.archlinux.org/man/pacstrap.8) installieren wir die "Base" und den Linux Kernel zu der Partition /mnt, wo wir später unser System haben werden. Anstatt linux kann man auch linux-lts für den LTS Kernel eingeben.

# FSTAB

["fstab"](https://wiki.archlinux.org/title/Fstab) steht für "File System Table" und um den zu generieren muss man folgendes machen:
```
genfstab -U /mnt >> /mnt/etc/fstab
```
">>" heißt, dass etwas "append-ed" wird. Es definiert in diesem Fall einfach nur wo es unseren fstab generieren soll. "-U" ist eine sogenannte "Flag", welche definiert, wie dieser fstab generiert werden soll. Dazu werde ich hier nicht ins Detail gehen.

# arch-chroot

Jetzt wo wir unserem System definiert haben, wie unser fstab aussehen soll, können wir uns als root User in unseren Mountpoint /mnt rooten. Was einfach nur heißt, dass wir uns nicht mehr im USB Stick befinden, sondern in unserem System. Jetzt haben wir den schwierigsten Teil hinter uns.
```
arch-chroot /mnt
```

Jetzt wird unsere Terminal Prompt anders aussehen und sollte nicht merh rot sein.

# Zoneinfo

Wir sagen hier unserem System, wo wir uns befinden, damit es die Zeit und weitere Sachen passend anzeigen und verstehen kann.
```
ln -sf /usr/share/zoneinfo/REGION/CITY /etc/localtime

(Zum Beispiel: ln -sf /usr/share/zoneinfo/Slovakia/Bratislava /etc/localtime)

"ln" linked unsere Angabe zu /etc/localtime
"-sf" eine Flag welche definiert wie es gelinked werden soll
In /usr/share/zoneinfo/ befinden sich alle globalen Zoneinfos
```

# Hardware Clock

Unser System soll mit unserer Hardware Uhr [synchronisiert](https://www.duden.de/rechtschreibung/synchronisieren) werden...
```
hwclock --systohc
```

# Locale

Definition des Wortes [Locale](https://wiki.archlinux.org/title/Locale).
In meinem Fall will ich, dass mein System amerikanisch Englisch ist, was die Originalsprache ist. Ich empfehle, dass man es auch so macht, da Errormeldungen in der gleichen Sprache sind und so kann ich auf dem Internet einfacher eine Lösung finden.
```
pacman -S nano    (Wir installieren den Texteditor "nano")
nano /etc/locale.gen
```
Hier wirst du sehr viele Locales sehen. Um deinen auszusuchen, muss man einfach das "#" vor dem gewünschten Locale entfernen.

In meinem Fall: 
```
(In Nano kannst du dich mit den Pfeilen deiner Tastatur bewegen)

en_US.UTF-8 UTF-8

ctrl+x                    (Nano verlassen)
y                         (Ja ich will diese Datei speichern)
"clear" oder "ctrl+l"     (Terminal leeren)
```
```
locale-gen
```
Unser Locale wird generiert
# Hostname

Hier werden wir unserem System sagen, wie unser PC heißen soll. Nach diesem Namen wird dein PC im Netzwerk identifiziert.
```
nano /etc/hostname    (Es ist eine neue File)
Hostname eingeben     (Alles klein und zusammen)

nano /etc/hosts       
```
In dieser Datei befinden sich 2 commented Lines. Wir fügen folgendes hinzu:
```
# Static table lookup for hostnames.
# See hosts(5) for details.

127.0.0.1    localhost
::1          localhost
127.0.1.1    HOSTNAME.localdomain    HOSTNAME
```
```
ctrl+x
y
(nano verlassen)
```
Hier setzt du dein HOSTNAME ein, welchen du in /etc/hosts eingegeben hast. Es muss genau so aussehen und bitte aufpassen das hier alles richtig geschrieben sind. Anstatt mehrmals Leertaste zu drücken, drücken wir TAB auf der Tastatur.
# Benutzer hinzufügen

Hier geben wir unserem root User ein Passwort und unserem User, welchen wir hinzufügen ebenso.
```
passwd            (root Passwort)

useradd -m USER   (Anstatt USER dein Username eingeben)

passwd USER       (Passwort für USER)

usermod -aG wheel,audio,video,storage,optical USER
```
Hier sagen wir unserem System, wofür unser USER berechtigt ist und was er machen darf.

Jetzt installieren wir "sudo" und bearbeiten eine Datei, welche definiert was unser USER unter dem sudo Command machen darf.
```
pacman -S sudo (sudo installieren)

EDITOR=nano visudo
```
Hier müssen wir die folgende Line uncommenten (das "#" entfernen). Wir finden und entfernen das "#" in der folgenden Line:
```
#%wheel ALL=(ALL) ALL

(nano verlassen)
```
Das besagt, dass unser USER alles machen kann, solange er sudo benutzt.
# GRUB installieren

Was ist [GRUB](https://wiki.archlinux.org/title/GRUB)? 

GRUB ist ein ["bootloader"](https://www.ionos.com/digitalguide/server/configuration/what-is-a-bootloader/). Windows zum Beispiel benutzt Bootmgr, doch auf Linux benutzt man meistens GRUB. Es gibt auch andere zur Auswahl. Ich empfehle nicht andere zu benutzen, wenn man sich nicht auskennt.

Grub installieren
```
pacman -S grub
```
Dadurch, dass unser System (wie die meisten Computer) UEFI-Boot verwendet müssen wir folgendes herunterladen:
```
pacman -S efibootmgr dosfstools mtools
```
So kann GRUB wissen, dass es auf einem UEFI-System installiert wird.

Jetzt machen wir ein Directory für unseren UEFI-Boot
```
mkdir /boot/EFI
```
Unsere EFI Partition "mounten"
```
mount /dev/YOURDEVICE1 /boot/EFI
```
Grub lokal installieren. Bitte ALLES richtig schreiben!
```
grub-install --target=x86_64-efi --bootloader-id=grub_uefi --recheck
```
GRUB wird informiert, dass es auf einem 64bit mit UEFI-Boot installiert wird.

Grub "Config File" erzeugen. Bitte alles RICHTIG schreiben.
```
grub-mkconfig -o /boot/grub/grub.cfg
```
".cfg" ist die Endung einer Configuration File.
# Abschließen

Bevor man rebootet sollte man jetzt [essenzielle](https://www.duden.de/rechtschreibung/essenziell) Software installieren.
```
pacman -S networkmanager (und andere Programme, welche du installieren willst)
```
Networkmanager[^4] mithilfe von ["Systemd"](https://wiki.archlinux.org/title/Systemd) aktivieren.
```
systemctl enable NetworkManager
```
Jetzt wird Networkmanager automatisch beim Booten aktiviert (Startup).

---
Wir verlassen "chroot"
```
exit
```
```
umount -l /mnt    (Vorher haben wir "mount" benutzt um reinzukommen. 
                   Jetzt benutzen wir "umount", um es wieder zu verlassen)
```


Jetzt entfernen wir unser USB Stick und rebooten unser System um in unsere brandneue Installation zu kommen!
```
reboot
```

Falls du soweit gekommen bist ohne Fehler, dann gratuliere ich dir. Du hast erfolgreich die Base von Archlinux installiert. Was du jetzt hast ist ein sehr minimales System ohne Display Server, Audio, Browser und den meisten alltäglichen Sachen, welche man auf Computers vorinstalliert hat. Man kann sich vorstellen man sei ein Künstler und was man vor sich hat ist ein weißes Blatt Papier. Mann kann alles selbser entscheiden und anpassen und mit seinem System Spaß haben.

## Was du alles gelernt hast

- [ ] Wie man ein Disk aufteilt
- [ ] Wie man ein Filesystem mounted
- [ ] Wie man mithilfe von pacman software installiert
- [ ] Wie man chroot verwendet
- [ ] FSTAB generieren
- [ ] Hostname setzen
- [ ] GRUB installieren
- [ ] Benutzer erstellen und ihnen root Rechte geben

# Ich danke

Carl, dass er mit mir die Informatik AG verwirklichen konnte!

Ich danke folgenden YouTubern, von denen ich sehr viel über Informatik, Linux, Programmieren und Computer Wissenschaft gelernt habe: 
- [Mental Outlaw](https://www.youtube.com/@MentalOutlaw)
- [DistroTube](https://www.youtube.com/@DistroTube)
- [Fireship](https://www.youtube.com/@Fireship)
- [Bro Code](https://www.youtube.com/@BroCodez)
- [Luke Smith](https://www.youtube.com/@LukeSmithxyz)
- [DorianDotSlash](https://www.youtube.com/@Doriandotslash)
- [DenshiVideo](https://www.youtube.com/@Denshi)
- Allen mit denen ich die Informatik AG haben konnte!

## Inspirationen

- Terry A. Davis
- Linus Torvalds
- Richard Stallman

### Websites

- [FSF](https://www.fsf.org/)
- [Github](https://github.com/)
- [ArchWiki](https://wiki.archlinux.org/)
- [GentooWiki](https://wiki.gentoo.org/wiki/Main_Page)


![](https://i.imgur.com/xlImqq2.jpg)

---
### Definitionen
[^1]: Falls du nicht weisst was du machen sollst kannst du m zur Hilfe eingeben. Fdisk ist auf der Archlinux ISO vorinstalliert und dient zum "Partitioning" von Disks.
[^2]: Die Größe wird hier in Megabite angegeben.
[^3]: Die 3. Partition muss man nicht ändern, da fdisk automatisch alle Partitions zu "Linux filesystem" macht, was bei der 3. passt, da es die "root" Partition ist (deswegen musste man Partitionen 1 und 2 ändern).
[^4]: Networkmanager zu installieren ist erst recht auf Laptops sehr wichtig, da man nicht immer einen LAN-Kabel zur Verfügung hat.
