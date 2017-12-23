#!/usr/bin/env python
import sys
import json


def main():
    if len(sys.argv) < 3:
        print("Usage: remove_tags {package_tag_map} {tag_to_remove}")
        return

    tag_file_path = sys.argv[1]
    tag_to_remove = sys.argv[2]

    json_content = []
    with open(tag_file_path, 'r') as tagfile:
        content = tagfile.read()
        json_content = json.loads(content)

        stacks = json_content[0]['package_topic_map']

        for key, stack in stacks.items():
            if tag_to_remove in set(stack):
                stack.remove(tag_to_remove)
                stacks[key] = stack
        print(stacks['com.github.downgoon:jresty-commons'])
    with open(tag_file_path, 'w') as tagfile:
        json_content[0]['package_topic_map'] = stacks
        tagfile.write(json.dumps(json_content, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
