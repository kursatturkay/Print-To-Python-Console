#https://www.youtube.com/watch?v=ZnxC3jXdo0E
#① console_clear() ② print() commands defined for this session. Clears or writes in Python Console rather than system console.
#① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ 
import bpy
import builtins as __builtin__
# Save the original print function
old_print = __builtin__.print

def console_print(*args):
    message = " ".join(map(str, args))
    
    for area in bpy.context.screen.areas:
        if area.type == 'CONSOLE':
            # If the CONSOLE area exists, write to it
            with bpy.context.temp_override(area=area):
                for line in message.split("\n"):
                    bpy.ops.console.scrollback_append(text=line)
            return
    
    # If the CONSOLE area does not exist, use the original print function
    old_print("Python Console area not found.")
    old_print(message)

def clear_console():
    for area in bpy.context.screen.areas:
        if area.type == 'CONSOLE':
            # If the CONSOLE area exists, clear it
            with bpy.context.temp_override(area=area):
                bpy.ops.console.clear()
            return
    
    # If the CONSOLE area does not exist, print a warning message
    old_print("Python Console area not found, could not clear. Please switch to the 'Scripting' workspace and try again.")

def pprint(*args, **kwargs):
    # Redirect pprint to console_print
    console_print(*args)
    
# Redefine the print function as pprint
__builtin__.print = pprint

# Redefine the clear_console function
__builtin__.clear_console = clear_console
