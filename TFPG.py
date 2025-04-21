import random
from TFPG_TAGS import TAG_EXPANSIONS
from TFPG_CLASSIFICATIONS import CLASSIFICATIONS

class TokenFlow:
    @staticmethod
    def tag_input(text):
        text = text.lower()
        tags = []
        for keywords, tag in CLASSIFICATIONS:
            if any(keyword in text for keyword in keywords):
                tags.append(tag)
        return tags

    @staticmethod
    def expand_tags(tags):
        output = []
        for tag in tags:
            clean_tag = tag.strip("[]")
            options = TAG_EXPANSIONS.get(clean_tag)
            if options:
                output.append(random.choice(options))
            else:
                output.append(f"[Unknown:{clean_tag}]")
        return " ".join(output)

    @staticmethod
    def process(text):
        print(f"\n🔍 INPUT: {text}")
        tags = TokenFlow.tag_input(text)
        print(f"🔖 TAGS: {tags}")
        output = TokenFlow.expand_tags(tags)
        print(f"💬 OUTPUT: {output}")
        return output

if __name__ == "__main__":
    TokenFlow.process("Yo, What's the weather?")
    TokenFlow.process("Hello")
    TokenFlow.process("Goodbye")