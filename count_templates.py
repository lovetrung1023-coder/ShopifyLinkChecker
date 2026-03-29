import sys
sys.path.insert(0, 'utils')
from template_generator import PageTemplateGenerator

about_us_count = len(PageTemplateGenerator.ABOUT_US_TEMPLATES)
shipping_count = len(PageTemplateGenerator.SHIPPING_POLICY_TEMPLATES)
total = about_us_count + shipping_count

print(f"📊 Template Count:")
print(f"  About Us: {about_us_count}")
print(f"  Shipping Policy: {shipping_count}")
print(f"  Total: {total}")
print(f"  Target: 100")
print(f"  Remaining: {100 - total}")
