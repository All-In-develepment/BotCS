using Application.Core;
using AutoMapper;
using AutoMapper.QueryableExtensions;
using MediatR;
using Persistence;

namespace Application.Tips
{
    public class ListTipWithStatusTrue
    {
        public class Query : IRequest<Result<PagedList<TipDto>>>
        {
            public PagingParams Params { get; set; }
        }

        public class Handler :  IRequestHandler<Query, Result<PagedList<TipDto>>>
        {
            private readonly DataContext _context;
            private readonly IMapper _mapper;
            public Handler(DataContext context, IMapper mapper)
            {
                _mapper = mapper;
                _context = context;
            }

            public async Task<Result<PagedList<TipDto>>> Handle(Query request, CancellationToken cancellationToken)
            {
                var query = _context.Tips
                    .Where(t => t.TipStatus == true)
                    .OrderBy(d => d.TipDate)
                    .ProjectTo<TipDto>(_mapper.ConfigurationProvider)
                    .AsQueryable();

                return Result<PagedList<TipDto>>
                    .Success(await PagedList<TipDto>.CreateAsync(query,
                        request.Params.PageNumber, request.Params.PageSize));
            }
        }
    }
}