# minetest-depriv

### Features

- List all the players in auth.sqlite that have the specified privilege
- Optionally remove the privilege from all users that have it, some privs are seemingly stored outside of auth.sqlite so may require manual removal.


### Usage
List all players that have the 'fly' privilege
```$ python3 depriv.py -i /home/talamh/minetest/worlds/skyblock -p fly```
Remove the 'fly' privilege from all players
```$ python3 depriv.py -i /home/talamh/minetest/worlds/skyblock -p fly -r```

### TODO
Add ability to remove privilege from a specified player.
