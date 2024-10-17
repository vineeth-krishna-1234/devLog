class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash_map = {}
        for char in magazine:
            magazine_hash_map[char] = magazine_hash_map.get(char, 0) + 1
        ransomeNote_hash_map = {}
        for char in ransomNote:
            ransomeNote_hash_map[char] = ransomeNote_hash_map.get(char, 0) + 1
        for key, value in ransomeNote_hash_map.items():
            if not magazine_hash_map.get(key, 0) >= value:
                return False

        return True
