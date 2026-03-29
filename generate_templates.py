"""
Script to generate additional templates for template_generator.py
This will create 40 new About Us templates and 44 new Shipping Policy templates
"""

# Additional About Us Templates (40 new ones)
ADDITIONAL_ABOUT_US = [
    # Startup & Innovation (5)
    {"name": "Disruptive Innovator", "tone": "startup", "focus": "innovation"},
    {"name": "Tech-First Pioneer", "tone": "startup", "focus": "technology"},
    {"name": "Agile Challenger", "tone": "startup", "focus": "disruption"},
    {"name": "Digital Native", "tone": "startup", "focus": "digital"},
    {"name": "Future-Focused Venture", "tone": "startup", "focus": "future"},
    
    # Artisan & Handcrafted (5)
    {"name": "Master Craftsman", "tone": "artisan", "focus": "quality"},
    {"name": "Heritage Maker", "tone": "artisan", "focus": "tradition"},
    {"name": "Handmade Excellence", "tone": "artisan", "focus": "craftsmanship"},
    {"name": "Artisan Collective", "tone": "artisan", "focus": "community"},
    {"name": "Timeless Craft", "tone": "artisan", "focus": "heritage"},
    
    # Budget-Friendly (5)
    {"name": "Value Champion", "tone": "budget", "focus": "affordability"},
    {"name": "Smart Shopper's Choice", "tone": "budget", "focus": "savings"},
    {"name": "Everyday Essentials", "tone": "budget", "focus": "practical"},
    {"name": "Accessible Quality", "tone": "budget", "focus": "value"},
    {"name": "Budget-Conscious Brand", "tone": "budget", "focus": "economy"},
    
    # Health & Wellness (5)
    {"name": "Wellness Advocate", "tone": "health", "focus": "wellbeing"},
    {"name": "Natural Living", "tone": "health", "focus": "organic"},
    {"name": "Holistic Health Hub", "tone": "health", "focus": "holistic"},
    {"name": "Clean & Green", "tone": "health", "focus": "sustainability"},
    {"name": "Mindful Choices", "tone": "health", "focus": "mindfulness"},
    
    # Adventure & Outdoor (5)
    {"name": "Adventure Seeker", "tone": "adventure", "focus": "exploration"},
    {"name": "Outdoor Enthusiast", "tone": "adventure", "focus": "nature"},
    {"name": "Trail Blazer", "tone": "adventure", "focus": "adventure"},
    {"name": "Wild & Free", "tone": "adventure", "focus": "freedom"},
    {"name": "Explorer's Haven", "tone": "adventure", "focus": "discovery"},
    
    # Minimalist & Modern (5)
    {"name": "Essential Minimalist", "tone": "minimal", "focus": "simplicity"},
    {"name": "Clean Lines", "tone": "minimal", "focus": "design"},
    {"name": "Less Is More", "tone": "minimal", "focus": "minimalism"},
    {"name": "Modern Simplicity", "tone": "minimal", "focus": "contemporary"},
    {"name": "Refined Essentials", "tone": "minimal", "focus": "refinement"},
    
    # Community-Driven (5)
    {"name": "Community First", "tone": "community", "focus": "connection"},
    {"name": "Together We Thrive", "tone": "community", "focus": "collaboration"},
    {"name": "Collective Impact", "tone": "community", "focus": "impact"},
    {"name": "Shared Values", "tone": "community", "focus": "values"},
    {"name": "People-Powered", "tone": "community", "focus": "people"},
    
    # Educational & Informative (5)
    {"name": "Knowledge Sharer", "tone": "educational", "focus": "learning"},
    {"name": "Expert Guide", "tone": "educational", "focus": "expertise"},
    {"name": "Informed Choices", "tone": "educational", "focus": "information"},
    {"name": "Learning Journey", "tone": "educational", "focus": "education"},
    {"name": "Empowered Consumer", "tone": "educational", "focus": "empowerment"},
]

# Additional Shipping Policy Templates (44 new ones)
ADDITIONAL_SHIPPING = [
    # FAQ Style (8)
    {"name": "FAQ Comprehensive", "style": "faq"},
    {"name": "Q&A Format", "style": "faq"},
    {"name": "Common Questions", "style": "faq"},
    {"name": "Your Questions Answered", "style": "faq"},
    {"name": "Shipping FAQs", "style": "faq"},
    {"name": "Quick Answers", "style": "faq"},
    {"name": "Everything You Need to Know", "style": "faq"},
    {"name": "Shipping Guide Q&A", "style": "faq"},
    
    # Timeline Visual (8)
    {"name": "Journey Timeline", "style": "timeline"},
    {"name": "Step-by-Step Process", "style": "timeline"},
    {"name": "Delivery Roadmap", "style": "timeline"},
    {"name": "Your Order's Path", "style": "timeline"},
    {"name": "Shipping Stages", "style": "timeline"},
    {"name": "From Us to You Timeline", "style": "timeline"},
    {"name": "Visual Journey", "style": "timeline"},
    {"name": "Tracking Your Package", "style": "timeline"},
    
    # Comparison Tables (8)
    {"name": "Shipping Options Compared", "style": "table"},
    {"name": "Delivery Methods Table", "style": "table"},
    {"name": "Speed vs Cost", "style": "table"},
    {"name": "Regional Comparison", "style": "table"},
    {"name": "Service Levels", "style": "table"},
    {"name": "At-a-Glance Shipping", "style": "table"},
    {"name": "Quick Reference Table", "style": "table"},
    {"name": "Shipping Matrix", "style": "table"},
    
    # Story-Based (8)
    {"name": "The Journey Story", "style": "story"},
    {"name": "Behind the Scenes", "style": "story"},
    {"name": "A Day in Shipping", "style": "story"},
    {"name": "From Warehouse to Doorstep", "style": "story"},
    {"name": "The Delivery Tale", "style": "story"},
    {"name": "Your Package's Adventure", "style": "story"},
    {"name": "Shipping Chronicles", "style": "story"},
    {"name": "The Fulfillment Story", "style": "story"},
    
    # Problem-Solution (8)
    {"name": "Worry-Free Shipping", "style": "problem-solution"},
    {"name": "Addressing Your Concerns", "style": "problem-solution"},
    {"name": "Solutions to Common Issues", "style": "problem-solution"},
    {"name": "Peace of Mind Delivery", "style": "problem-solution"},
    {"name": "Overcoming Shipping Challenges", "style": "problem-solution"},
    {"name": "Your Concerns, Our Solutions", "style": "problem-solution"},
    {"name": "Hassle-Free Guarantee", "style": "problem-solution"},
    {"name": "Smooth Delivery Promise", "style": "problem-solution"},
    
    # Data-Driven (4)
    {"name": "By the Numbers", "style": "data"},
    {"name": "Statistics & Facts", "style": "data"},
    {"name": "Proven Performance", "style": "data"},
    {"name": "Data-Backed Delivery", "style": "data"},
]

print(f"Generated {len(ADDITIONAL_ABOUT_US)} About Us templates")
print(f"Generated {len(ADDITIONAL_SHIPPING)} Shipping Policy templates")
print(f"Total: {len(ADDITIONAL_ABOUT_US) + len(ADDITIONAL_SHIPPING)} new templates")
