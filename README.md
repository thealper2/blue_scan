# blue_scan

Etraftaki bluetooth cihazlarını bulmaya yarayan bir araçtır.

## Gereksinimler

blue_scan aşağıdaki kütüphaneleri kullanır.

* Colorama
* PyBluez

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/blue_scan.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| --scan    | Bluetooth taraması. |
| --target  | Bulunmak istenen cihazın Bluetooth adı |

```bash
usage: blue_scan.py [-h] [--scan] [--target TARGET]

BT Scan

options:
  -h, --help       show this help message and exit
  --scan           Scan devices.
  --target TARGET  Find Target device.
```

## Örnekler

```python
python3 blue_scan.py --scan
pyton3 blue_scan.py --target 'Alper Iphone'
```
