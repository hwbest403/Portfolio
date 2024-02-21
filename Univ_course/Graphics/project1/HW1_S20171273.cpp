#include <stdio.h>
#include <stdlib.h>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include <math.h>

#define _CRT_SECURE_NO_WARNINGS

#define MAX_POINT 128

float initial_width = 800.0, initial_height = 600.0;
float current_width = 800.0, current_height = 600.0;
int prev_x = 0, prev_y = 0;
int rightbuttonpressed = 0;

float point[MAX_POINT][2];
int point_count = 0;
float center[2];

float angle = 0.03f;

int shift_flag = 0;
int p_flag = 0;
int center_flag = 0;
int rotate_flag = 0;

float r = 80.0f / 255.0f, g = 200.0f / 255.0f, b = 120.0f / 255.0f; // Background color = green

void Timer(int value) {
	glutPostRedisplay();
	glutTimerFunc(100, Timer, 1);
}

void display(void) {
	glClearColor(r, g, b, 1.0f); 
	glClear(GL_COLOR_BUFFER_BIT);

	if (point_count > 0) {
		for (int i = 0; i < point_count; i++) {
			glColor3f(0, 0, 255);
			glPointSize(5.0f);
			glBegin(GL_POINTS);
			glVertex2f(point[i][0],point[i][1]);
			glEnd();
		}
	}

	if (point_count > 1) {
		for (int i = 0; i < point_count - 1; i++) {
			glColor3f(128, 0, 0);
			glLineWidth(1.0f);
			glBegin(GL_LINES);
			glVertex2f(point[i][0],point[i][1]);
			glVertex2f(point[i+1][0], point[i+1][1]);
			glEnd();
		}
	}

	if (center_flag == 1) {
		glColor3f(255, 255, 0);
		glPointSize(5.0f);
		glBegin(GL_POINTS);
		glVertex2f(center[0], center[1]);
		glEnd();
	}

	if (rotate_flag == 1) {
		for (int i = 0; i < point_count; i++) {
			float tmpx, tmpy;
			point[i][0] = point[i][0] - center[0];
			point[i][1] = point[i][1] - center[1];
			tmpx = point[i][0] * cos(angle) - point[i][1] * sin(angle);
			tmpy = point[i][0] * sin(angle) + point[i][1] * cos(angle);
			point[i][0] = tmpx + center[0];
			point[i][1] = tmpy + center[1];
		}
	}

	glFlush();
}

void keyboard(unsigned char key, int x, int y) {
	if (rotate_flag == 0) {
		if (key == 'c') {
			for (int i = 0; i < point_count; i++) {
				point[i][0] = NULL;
				point[i][1] = NULL;
			}
			point_count = 0;
			p_flag = 0;
			glutPostRedisplay();
		}
		if (key == 'p') {
			if (point_count < 3) {
				fprintf(stdout, "*** Choose at least three points!\n");
			}
			else {
				point[point_count][0] = point[0][0];
				point[point_count][1] = point[0][1];
				point_count++;
				p_flag = 1;
			}
			glutPostRedisplay();
		}
	}
	if (p_flag == 1) {
		if (key == 'r') {
			if (rotate_flag == 0) {
				float area = 0.0;
				float k;
				for (int i = 0; i < point_count - 1; i++) {
					k = ((point[i][0] * point[i + 1][1]) - (point[i + 1][0] * point[i][1]));
					area = area + k;
					k = ((point[i][0] + point[i + 1][0]) * (point[i][0] * point[i + 1][1] - point[i + 1][0] * point[i][1]));
					center[0] = center[0] + k;
					k = ((point[i][1] + point[i + 1][1]) * (point[i][0] * point[i + 1][1] - point[i + 1][0] * point[i][1]));
					center[1] = center[1] + k;
				}
				area = area / 2.0;
				area = area * 6.0;
				area = (1.0 / area);
				center[0] = area * center[0];
				center[1] = area * center[1];
				center_flag = 1;
				rotate_flag = 1;
				glutPostRedisplay();
			}
			else if (rotate_flag == 1) {
				center[0] = NULL;
				center[1] = NULL;
				center_flag = 0;
				rotate_flag = 0;
				glutPostRedisplay();
			}
		}
	}
	if (key == 'f') {
		glutLeaveMainLoop();
	}
}

void special(int key, int x, int y) {
	if (p_flag == 1 && rotate_flag==0 ) {
		switch (key) {
		case GLUT_KEY_LEFT:
			for (int i = 0; i < point_count; i++) {
				point[i][0] = point[i][0] - 0.05;
			}
			glutPostRedisplay();
			break;
		case GLUT_KEY_RIGHT:
			for (int i = 0; i < point_count; i++) {
				point[i][0] = point[i][0] + 0.05;
			}
			glutPostRedisplay();
			break;
		case GLUT_KEY_DOWN:
			for (int i = 0; i < point_count; i++) {
				point[i][1] = point[i][1] - 0.05;
			}
			glutPostRedisplay();
			break;
		case GLUT_KEY_UP:
			for (int i = 0; i < point_count; i++) {
				point[i][1] = point[i][1] + 0.05;
			}
			glutPostRedisplay();
			break;
		}
	}
}

void mousepress(int button, int state, int x, int y) {
	if ((glutGetModifiers()==GLUT_ACTIVE_SHIFT) && (button == GLUT_LEFT_BUTTON) && (state == GLUT_DOWN) && (p_flag==0) && (rotate_flag==0) ) {
		point[point_count][0] = (float)x / current_width;
		point[point_count][1] = (float)(current_height - (float)y) / current_height;
		point[point_count][0] = (point[point_count][0] - 0.5) * 2.0;
		point[point_count][1] = (point[point_count][1] - 0.5) * 2.0;
		point_count++;
		glutPostRedisplay();
	}
	else if ((button == GLUT_RIGHT_BUTTON) && (state == GLUT_DOWN)) {
		rightbuttonpressed = 1;
		prev_x = x, prev_y = y;
	}
	else if ((button == GLUT_RIGHT_BUTTON) && (state == GLUT_UP)) {
		rightbuttonpressed = 0;
	}
}

void mousemove(int x, int y) {
	if (rightbuttonpressed && (rotate_flag==0) && (p_flag==1)) {
		int del_x = x - prev_x, del_y = y - prev_y;
		if (p_flag == 1) {
			for (int i = 0; i < point_count; i++) {
				point[i][0] = point[i][0] + ((float)del_x / current_width)*2.0;
				point[i][1] = point[i][1] - ((float)del_y / current_height)*2.0;
			}
			glutPostRedisplay();
		}
		prev_x = x, prev_y = y;
	}
}
	
void reshape(int width, int height) {
	fprintf(stdout, "### The new window size is %dx%d.\n", width, height);
	current_width = width;
	current_height = height;
	glViewport(0.0, 0.0, width, height); 
	glLoadIdentity();
}

void close(void) {
	fprintf(stdout, "\n^^^ The control is at the close callback function now.\n\n");
}

void register_callbacks(void) {
	glutDisplayFunc(display);
	glutKeyboardFunc(keyboard);
	glutSpecialFunc(special);
	glutMouseFunc(mousepress);
	glutMotionFunc(mousemove);
	glutReshapeFunc(reshape);
 	glutCloseFunc(close);
}

void initialize_renderer(void) {
	register_callbacks();
}

void initialize_glew(void) {
	GLenum error;

	glewExperimental = TRUE;
	error = glewInit();
	if (error != GLEW_OK) {
		fprintf(stderr, "Error: %s\n", glewGetErrorString(error));
		exit(-1);
	}
	fprintf(stdout, "*********************************************************\n");
	fprintf(stdout, " - GLEW version supported: %s\n", glewGetString(GLEW_VERSION));
	fprintf(stdout, " - OpenGL renderer: %s\n", glGetString(GL_RENDERER));
	fprintf(stdout, " - OpenGL version supported: %s\n", glGetString(GL_VERSION));
	fprintf(stdout, "*********************************************************\n\n");
}

void greetings(char *program_name, char messages[][256], int n_message_lines) {
	fprintf(stdout, "**************************************************************\n\n");
	fprintf(stdout, "  PROGRAM NAME: %s\n\n", program_name);

	for (int i = 0; i < n_message_lines; i++)
		fprintf(stdout, "%s\n", messages[i]);
	fprintf(stdout, "\n**************************************************************\n\n");

	initialize_glew();
}

#define N_MESSAGE_LINES 4
void main(int argc, char* argv[]) {
	char program_name[64] = "Sogang CSE4170 20171273 HW1";
	char messages[N_MESSAGE_LINES][256] = {
		"    - Keys used: 'shift', 'p', 'c', 'r', 'f'",
		"    - Special keys used: LEFT, RIGHT, UP, DOWN",
		"    - Mouse used: L-click, R-click",
		"    - Other operations: window size change"
	};

	glutInit(&argc, argv);
	glutInitContextVersion(4, 0);
	glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE); // <-- Be sure to use this profile for this example code!
 //	glutInitContextProfile(GLUT_CORE_PROFILE);

	glutInitDisplayMode(GLUT_RGBA);

	glutInitWindowSize(initial_width, initial_height);
	glutInitWindowPosition(550, 200);
	glutCreateWindow(program_name);

	greetings(program_name, messages, N_MESSAGE_LINES);
	initialize_renderer();
	glutTimerFunc(100, Timer, 1);

	// glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_EXIT); // default
	glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS);

	glutMainLoop();
	fprintf(stdout, "^^^ The control is at the end of main function now.\n\n");
}