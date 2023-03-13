# Informatik AG 14.3.2023
**Eine OS selber bauen**
[Anleitung](https://wiki.archlinux.org/title/Installation_guide)
---
# Wie fange ich eigentlich an?
- Internet testen
```
ping gnu.org
```
- Systemuhr einstellen
```
timedatectl (auf output warten)
timedatectl-set ntp true (falls es falsch war)
```
- Drive formattieren und vorbereiten (Man wird beim Formattieren des Disks seine Daten verlieren!)
Am Anfang ist es wichtig zu wissen wie ein File System überhaupt aussehen soll. Man kann diverse Mittel benutzen um den zu formatieren und anzupassen. Man kann zum Beispiel [fdisk](https://www.geeksforgeeks.org/disk-partitioning-in-linux/) verwenden.
```
fdisk --help (falls unsicher)
```
```
 UEFI with GPT Mount point 	Partition 	Partition type 	Suggested size
/mnt/boot1 	/dev/efi_system_partition 	EFI system partition 	At least 300 MiB. If multiple kernels will be installed, then no less than 1 GiB.
[SWAP] 	/dev/swap_partition 	Linux swap 	More than 512 MiB
/mnt 	/dev/root_partition 	Linux x86-64 root (/) 	Remainder of the device

    Other mount points, such as /mnt/efi, are possible, provided that the used boot loader is capable of loading the kernel and initramfs images from the root volume. See the warning in Arch boot process#Boot loader.

BIOS with MBR Mount point 	Partition 	Partition type 	Suggested size
[SWAP] 	/dev/swap_partition 	Linux swap 	More than 512 MiB
/mnt 	/dev/root_partition 	Linux 	Remainder of the device 
```
[Quelle](https://wiki.archlinux.org/title/Installation_guide#Partition_the_disks)
- Hier ist es wichtig zu wissen ob man ein UEFI oder BIOS System hat, doch so ziemlich alle modernen Computer benutzen UEFI, also sollte man sich da keine Sorgen machen. Anhand dessen wird man sein Disk formatieren und den Layout machen.
[Quelle](https://wiki.archlinux.org/title/Installation_guide#Format_the_partitions)