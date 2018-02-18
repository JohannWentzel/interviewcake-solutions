
def rectIntersect(rect1, rect2):
		
	x = 0
	y = 0
	width = -1
	height = -1

	height1 = rect1["height"]
	height2 = rect2["height"]
	width1 = rect1["width"]
	width2 = rect2["width"]

	x1 = rect1["left_x"]
	x2 = rect2["left_x"]
	y1 = rect1["bottom_y"]
	y2 = rect2["bottom_y"]

	top1 = y1 + height1
	top2 = y2 + height2
	right1 = x1 + width1
	right2 = x2 + width2

	x = max(x1, x2)
	y = max(y1, y2)
	width =  min(right1 - x2, right2 - x1)
	height = min(top1 - y2, top2 - y1)




	return {
		'left_x': x,
		'bottom_y': y,
		'width': width,
		'height': height
	}

if __name__ == '__main__':
	rect1 = {
		'left_x': 0,
		'bottom_y': 0,
		'width': 300,
		'height': 600
	}
	rect2 = {
		'left_x': 5,
		'bottom_y': 2,
		'width': 3,
		'height': 6
	}

	intersect = rectIntersect(rect1, rect2)

	if intersect['width'] > 0:
		print("x =",intersect["left_x"], ", y = ", intersect["bottom_y"])
		print("width = ", intersect["width"], ", height = ",intersect["height"])	
	else:
		print("Rectangles do not overlap")	

	


