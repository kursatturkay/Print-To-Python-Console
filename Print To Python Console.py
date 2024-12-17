#https://www.youtube.com/watch?v=ZnxC3jXdo0E
#① console_clear() ② print() commands defined for this session. Clears or writes in Python Console rather than system console.
#① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ 
import bpy
import builtins as __builtin__

def console_print(*args):
    message = " ".join(map(str, args))
    
    for area in bpy.context.screen.areas:
        if area.type == 'CONSOLE':
            
            with bpy.context.temp_override(area=area):
                for line in message.split("\n"):
                    bpy.ops.console.scrollback_append(text=line)
            return
    
    __builtin__.print("Python Console alanı bulunamadı.")

def clear_console():
    for area in bpy.context.screen.areas:
        if area.type == 'CONSOLE':
            
            with bpy.context.temp_override(area=area):
                bpy.ops.console.clear()
            return
    
    __builtin__.print("Python Console Area not found, could not cleared. Switch WorkSpage To Scripting before retry")

def pprint(*args, **kwargs):
    console_print(*args)
    
__builtin__.print = pprint

print("clear_console() and print() redefined. Now print function writes in Builtin Python Console print(\"Some Info\") in this session only.")

__builtin__.clear_console = clear_console