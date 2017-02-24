function [path] = shortest_path(costs)

%
% given a 2D array of costs, compute the minimum cost vertical path
% from top to bottom which, at each step, either goes straight or
% one pixel to the left or right.
%
% costs:  a HxW array of costs
%
% path: a Hx1 vector containing the indices (values in 1...W) for 
%       each step along the path
%
%
%

map = zeros(size(costs)); % map of path cost
[h,w,~] = size(costs);
for x = 1: w
    map(1,x) = costs(1,x);  % the cost to the top level grid
                            % is just the cost
end
for y = 2: h
    map(y,1) = costs(y,1)+ min(map(y-1,1),map(y-1,2));
    % cost of leftmost one in y row = costs(grid) + min(up, rightup)
    map(y,w) = costs(y,w) + min(map(y-1,w), map(y-1,w-1));
    % cost of rightmost one in y row = costs(grid) + min(up, leftup)
    for x = 2: w-1
        map(y,x) = costs(y,x) + min([map(y-1,x-1),map(y-1,x),map(y-1,x+1)]);
        % cost of the grid (y,x) is:
                    %costs(grid) + min(leftup, up, rightup)
    end
end

% start backtracking
path = zeros(h,1);
% find start one
start = map(h,1);
path(h) = 1;
for x =2:w
    if map(h,x) < start
        start = map(h,x);
        path(h) = x;
    end
end

for y = h-1:-1:1
    start = map(y,path(y+1));
    path(y) = path(y+1);
    for x = path(y+1)-1:path(y+1)+1
        if x >=1 && x<= w
            if map(y,x) < start
                start = map(y,x);
                path(y) = x;
            end
        end
    end
end

