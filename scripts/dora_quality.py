"""Three executable DQ checks for clearly synthetic sample extracts."""
import csv, sys
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'data'/'synthetic'
def load(name):
 with (ROOT/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def check_unique_ids(rows, field): return len(rows)>0 and len({r[field] for r in rows})==len(rows)
def check_required(rows, fields): return all(all(r.get(k,'').strip() for k in fields) for r in rows)
def check_valid_time_and_values(deployments, incidents):
 try:
  for r in deployments:
   datetime.fromisoformat(r['deployed_at'].replace('Z','+00:00'))
   if float(r['lead_time_hours']) < 0 or r['change_failed'] not in {'0','1'}: return False
  for r in incidents:
   start=datetime.fromisoformat(r['started_at'].replace('Z','+00:00')); end=datetime.fromisoformat(r['resolved_at'].replace('Z','+00:00'))
   if end < start or r['caused_by_deployment'] not in {'0','1'}: return False
  return True
 except (ValueError,KeyError): return False
def main():
 d=load('deployments.csv'); i=load('incidents.csv')
 checks={'unique deployment/incident keys':check_unique_ids(d,'deployment_id') and check_unique_ids(i,'incident_id'), 'required fields populated':check_required(d,['deployment_id','service','deployed_at']) and check_required(i,['incident_id','service','started_at','resolved_at']), 'valid timestamps and nonnegative lead time/binary flags':check_valid_time_and_values(d,i)}
 for n,ok in checks.items(): print(('PASS' if ok else 'FAIL')+' - '+n)
 return 0 if all(checks.values()) else 1
if __name__=='__main__': sys.exit(main())
