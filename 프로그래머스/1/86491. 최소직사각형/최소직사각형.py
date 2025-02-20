def solution(sizes):
    max_width,max_height=0,0
    
    for width,height in sizes:
        if width>=height:
            max_width=max(max_width,width)
            max_height=max(max_height,height)
        else:
            max_width=max(max_width,height)
            max_height=max(max_height,width)
    
        
    return max_width*max_height