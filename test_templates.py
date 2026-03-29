"""
Quick test to verify template rotation works
"""
import sys
import os

# Add utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))

try:
    from template_generator import PageTemplateGenerator
    
    print("=" * 60)
    print("TEMPLATE COUNT VERIFICATION")
    print("=" * 60)
    
    about_count = len(PageTemplateGenerator.ABOUT_US_TEMPLATES)
    shipping_count = len(PageTemplateGenerator.SHIPPING_POLICY_TEMPLATES)
    total = about_count + shipping_count
    
    print(f"\n📊 Current Template Counts:")
    print(f"   About Us Templates: {about_count}")
    print(f"   Shipping Policy Templates: {shipping_count}")
    print(f"   Total Templates: {total}")
    print(f"   Target: 100")
    print(f"   Remaining to add: {max(0, 100 - total)}")
    
    print("\n" + "=" * 60)
    print("ROTATION MECHANISM TEST")
    print("=" * 60)
    
    # Test rotation for General templates
    print("\nGenerating 3 General About Us templates:")
    seen_general = []
    for i in range(3):
        result = PageTemplateGenerator.get_random_about_us_template(
            "Test Store", 
            "test@example.com",
            "Facebook | Instagram | Twitter",
            "hiking gear" # not fashion
        )
        template_name = result['template_name']
        seen_general.append(template_name)
        print(f"  {i+1}. {template_name}")

    # Test rotation for Fashion templates
    print("\nGenerating 3 Fashion About Us templates:")
    seen_fashion = []
    for i in range(3):
        result = PageTemplateGenerator.get_random_about_us_template(
            "Test Store", 
            "test@example.com",
            "Facebook | Instagram | Twitter",
            "Women's Clothing" # triggers fashion pool
        )
        template_name = result['template_name']
        seen_fashion.append(template_name)
        print(f"  {i+1}. {template_name}")
    
    # Check for duplicates
    if len(seen_general) == len(set(seen_general)) and len(seen_fashion) == len(set(seen_fashion)):
        print("\n✅ SUCCESS: No duplicates in either pool!")
    else:
        print("\n⚠️  WARNING: Found duplicates")
    
    print("\n" + "=" * 60)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
