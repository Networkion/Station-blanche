from pprint import pprint
from yara_scanner import YaraScanner

scanner = YaraScanner()
# tells the scanner to start tracking this yara file
scanner.track_yara_dir('modules/yara/rules')
scanner.load_rules()

# Ajout du scan du fichier 'import_hash.py'
if scanner.scan('../../../../../import_hash.py'):
    pprint(scanner.scan_results)

# Vérification si des fichiers YARA suivis ont changé
if scanner.check_rules():
    scanner.load_rules()